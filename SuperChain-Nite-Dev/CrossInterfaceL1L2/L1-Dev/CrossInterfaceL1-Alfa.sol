// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface CrossInterfaceL1L2-Alfa {
    function xDomainMessageSender() external view returns (address);
    function sendMessage(
        address _target,
        bytes calldata _message,
        uint32 _gasLimit
    ) external;
}

contract Greeter {
    CrossInterfaceL1L2-Alfa public immutable MESSENGER;
    Greeter public immutable OTHER_ORIGIN;
    mapping (address => string) public data;

    constructor(
        CrossInterfaceL1L2-Alfa _messenger,
        Greeter _otherGreeter
    ) {
        MESSENGER = _messenger;
        OTHER_ORIGIN = _otherGreeter;
    }

    function sendGreeting(string memory _databank) public {
        MESSENGER.sendMessage(
            address(OTHER_ORIGIN),
            abi.encodeCall(
                this.setGreeting,
                (
                    msg.sender,
                    _databank
                )
            ),
            200000
        );
    }

    function setGreeting(address _sender, string memory _databank) public {
        require(
            msg.sender == address(MESSENGER),
            "Greeter: Direct sender must be the CrossDomainMessenger"
        );

        require(
            MESSENGER.xDomainMessageSender() == address(OTHER_ORIGIN),
            "Greeter: Remote sender must be the other Greeter contract"
        );

        data[_sender] = _greeting;
    }
}