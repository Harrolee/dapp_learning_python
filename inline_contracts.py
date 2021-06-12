# this is the solidity compiler
# https://pypi.org/project/py-solc/
from solc import compile_standard

# Solidity source code
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "Greeter.sol": {
            "content": '''
                pragma solidity ^0.8.0;

                contract Greeter {
                string public greeting;

                constructor() public {
                    greeting = 'Hello';
                }

                function setGreeting(string memory _greeting) public {
                    greeting = _greeting;
                }

                function greet() view public returns (string memory) {
                    return greeting;
                }
                }
            '''
        }
    },
    "settings":
        {
            "outputSelection": {
                "*": {
                    "*": [
                        "metadata", "evm.bytecode"
                        , "evm.bytecode.sourceMap"
                    ]
                }
            }
        }
    })

# fiddle with these arguments: https://docs.soliditylang.org/en/develop/using-the-compiler.html#compiler-input-and-output-json-description
compiled_sol_nft = compile_standard({
    "language": "Solidity",
    "sources": {
        "MyNFT.sol": { 
            "urls":
                [
                    # how will the ipfs url be used??
                    
                    #"bzzr://56ab...",
                    #"ipfs://Qma...",
                    "contracts/MyNFT.sol"
                    #// If files are used, their directories should be added to the command line via
                    #// `--allow-paths <path>`.
                ]
        }
    },
    "settings":
        {
            "outputSelection": {
                "*": {
                    "*": [
                        "metadata", "evm.bytecode"
                        , "evm.bytecode.sourceMap"
                    ]
                }
            }
        }
    })