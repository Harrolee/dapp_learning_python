// from this tutorial: https://docs.alchemy.com/alchemy/tutorials/how-to-create-an-nft#step-2-create-your-app-and-api-key
    // which is base on this tutorial: https://docs.openzeppelin.com/contracts/3.x/erc721 

// version of compiler to use
pragma solidity ^0.8.0;

// our contract will use other contracts
import "openzeppelin/contracts/token/ERC721/ERC721.sol";
import "openzeppelin/contracts/utils/Counters.sol";
import "openzeppelin/contracts/access/Ownable.sol";

// functions of type view do not write to blockchain. They do not cost gas.
// type pure: blockchain is not accessed or modified
// type payable: function can receive ether

/*
variables in a class are available without having to specify the namespace
    it is assumed that I am referencing objects in the namespace of the contract object
        I don't have to prefix object variable references with 'this'
*/

/*
    EVM and state:
        1 storage
            contract state variables are here.
            persists between calls
            expensive to use
        2 memory
            temp values. Think of as RAM
            erased between external function calls (what does this mean)????
        3 stack     --> for some reason, I was unable to use this in my function?
            small local variables
*/

contract MyNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor() public ERC721("MyNFT", "NFT") {}

    function mintNFT(address recipient, string memory tokenURI)
        public onlyOwner
        returns (uint256)
    {
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(recipient, newItemId);
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    }
}