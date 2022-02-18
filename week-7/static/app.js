let button=document.querySelector("section form button");
button.addEventListener("click", e =>{
    //阻止表單送出跳轉
    e.preventDefault(); 
    //先抓取查詢資料後要顯示查詢結果的div
    let result=document.querySelector("div.result");
    //預設每次查詢新username都要將上一次的結果刪除避免疊加顯示結果 
    if (result.childNodes[0]){
        result.removeChild(result.childNodes[0]);
    }
    
    //由於表單已被prevent無法從url獲得要求字串,改從表單索取
    let catchForm=new FormData(document.querySelector("form")); //建立FormData物件並偵測form元素
    let formData=catchForm.get("username");//抓取form中name=username的資料
    // 測試console.log(formData);
    //開始fetch API資料
    fetch("http://127.0.0.1:3000/api/members?username="+formData)
    .then(response=>{
        //將回應以JSON格式回傳
        let result=response.json(); //但不是很懂為何一定要用變數承接
        return result;
    })
    .then(data=>{
        //
        let getData=data;//不是很懂為何一定要用變數承接
        // console.log(getData["data"]["name"]);
        //準備將查詢到的資料顯示到畫面
        let resultData=document.createElement("p"); //創建p元素
        let text=getData["data"]["name"];//取JSON物件方式取值:name
        // console.log(text);
        //將結果以innerText新增至p元素
        resultData.innerText=text;
        //新增至指定div下
        result.appendChild(resultData);
        
    })
    .catch(error=>{
        let resultData=document.createElement("p");
        resultData.innerText="查無此人";
        result.appendChild(resultData);
    })  
})

