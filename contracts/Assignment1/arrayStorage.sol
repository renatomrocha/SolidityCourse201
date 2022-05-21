pragma solidity ^0.8.0;


contract ArrayStorage {


    Entity[] public entitiesArray;

    struct Entity{
        uint data;
        address _address;
    } 

  function addEntity(uint data) external returns(bool) {
        entitiesArray.push(Entity(data, msg.sender));
        return true;
  }

  function updateEntity(uint data) external returns(bool) {
      Entity memory entityToUpdate;
      for (uint i=0; i< entitiesArray.length; i++) {
          if(entitiesArray[i]._address == msg.sender) {
            entityToUpdate = entitiesArray[i];
            entityToUpdate.data = data;
            entitiesArray[i] = entityToUpdate;
            break;
          }
      }
      return true;
  }


} 