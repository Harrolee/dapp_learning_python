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