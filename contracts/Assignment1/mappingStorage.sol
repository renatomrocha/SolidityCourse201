pragma solidity ^0.8.0;


contract MappingStorage {


    mapping(address => Entity) public entitiesMapping;

    struct Entity{
        uint data;
        address _address;
    } 

  function addEntity(uint data) external returns(bool) {
    //   require(entitiesMapping[msg.sender]._address == address(0), "Entity already created");
      entitiesMapping[msg.sender] = Entity(data, msg.sender);
        return true;
  }

  function updateEntity(uint data) external returns(bool) {
    //   require(entitiesMapping[msg.sender]._address!= address(0), "Entity does not exist");
      entitiesMapping[msg.sender].data = data;
      return true;
  }


} 