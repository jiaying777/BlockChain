pragma solidity ^0.6.0;

contract bankaccount{
    address payable owner;
    mapping(string => address ) public students;
    mapping(address => uint) public balances;
    mapping(address => string) public addr;
    
    
    constructor () public payable {
        owner = msg.sender;
    }
    
    //帳戶註冊
    function enroll(string memory studentId) public {
        require(students[studentId] == address(0), "The studentId is already used");
        require(bytes(addr[msg.sender]).length == 0, "The address is already used");
        students[studentId] = msg.sender;
        addr[msg.sender] = studentId;
        
        //註冊過的 studentId 和 address 不可重複註冊
    } 
    
    //存錢
    function deposit() public payable{
        require(bytes(addr[msg.sender]).length != 0, "Please register an account");
        balances[msg.sender] = balances[msg.sender]+msg.value;
        
        //若沒有註冊帳戶則不能存錢
    }
    
    //提錢
    function withdraw(uint withdrawAmount) public {
        require(bytes(addr[msg.sender]).length != 0, "Please register an account");
        require(balances[msg.sender] >= withdrawAmount, "Balances not enough");
        msg.sender.transfer(withdrawAmount);
        balances[msg.sender] = balances[msg.sender]-withdrawAmount;
        
        //沒有帳戶或餘額不足則無法領錢
    }
    
    //銀行內部轉帳
    function transfer(uint transferAmount, address transferTo) public{
        require(msg.sender != transferTo, "Can't transfer to yourself");
        require(bytes(addr[transferTo]).length != 0, "The transfer account not registered");
        require(balances[msg.sender] >= transferAmount, "Balances not enough");
        balances[msg.sender] = balances[msg.sender]-transferAmount;
        balances[transferTo] = balances[transferTo]+transferAmount;
        
        //不能轉帳給自己，也不能轉帳給沒有註，餘額不足也會轉帳失敗
    }
    
    //餘額查詢
    function getBalance() public view returns(uint){
        require(bytes(addr[msg.sender]).length != 0, "No account");
        return balances[msg.sender];
        
        //若沒有帳戶則無法查詢餘額
    }
    
    //銀行資產查詢
    function getBankBalance() public view returns(uint){
        require(msg.sender == owner,"Permission denied");
        return address(this).balance;
        
        //只有owner可以查詢銀行合約的餘額
    }
    
    
    fallback() external{
        require(owner == msg.sender, "Permission denied");
        selfdestruct(owner);
        
        //owner捲款潛逃，把合約裡剩餘的錢都轉給owner
    }
    
    //變更studentId
    function changeStudentId(string memory studentId) public {
        require(bytes(addr[msg.sender]).length != 0, "No account");
        require(students[studentId] == address(0), "The studentId is already used");
        delete students[addr[msg.sender]];
        students[studentId] = msg.sender;
        addr[msg.sender] = studentId;
        
        //需要有帳戶才可以更改studentId，已被使用的studentId不可使用
        //因為上面規定一個地址只能對應一個studentId，反之亦然，所以新增一個功能讓使用者可以變更studentId
        //此功能有點像變更個資
    }
    
