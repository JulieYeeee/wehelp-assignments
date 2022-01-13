function getData(){
    let req=new XMLHttpRequest;
    let url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
    req.open('GET',url);
    req.onload=function(){
    //處理JSON資料
    let data=JSON.parse(this.responseText);//將stringify過的資料還原
    let mainInfo=data["result"]["results"];//先抓出核心的景點資料

    for(i=0;i<8;i++){
        let title=mainInfo[i]["stitle"];
        let picSrc=mainInfo[i]["file"];
        let onePic=picSrc.split("https");
        // console.log(onePic);

        let itemsContainer=document.querySelector(".items-container");
        let items=document.createElement("div");
        items.classList.add("items");

        let picContainer=document.createElement("div");
        picContainer.classList.add("pic-container");

        let img=document.createElement("img");
        img.setAttribute("src","https"+onePic[1]);

        let newP=document.createElement("p");
        newP.innerText=title;
        newP.classList.add("item-title");

        itemsContainer.appendChild(items);
        items.appendChild(picContainer);
        picContainer.appendChild(img);
        items.appendChild(newP);
    
    }
}
req.send();
}

let count=7;
let clicks=1;
function moreData(){
    let req=new XMLHttpRequest;
    let url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
    req.open('GET',url);
    req.onload=function(){
    //處理JSON資料
    let data=JSON.parse(this.responseText);//將stringify過的資料還原
    let mainInfo=data["result"]["results"];//先抓出核心的景點資料
    clicks++;
    for(i=count+1;i<mainInfo.length;i++){
        count=i;
        
        let title=mainInfo[i]["stitle"];
        let picSrc=mainInfo[i]["file"];
        let onePic=picSrc.split("https");
        // console.log(onePic);

        let itemsContainer=document.querySelector(".items-container");
        let items=document.createElement("div");
        items.classList.add("items");

        let picContainer=document.createElement("div");
        picContainer.classList.add("pic-container");

        let img=document.createElement("img");
        img.setAttribute("src","https"+onePic[1]);

        let newP=document.createElement("p");
        newP.innerText=title;
        newP.classList.add("item-title");

        itemsContainer.appendChild(items);
        items.appendChild(picContainer);
        picContainer.appendChild(img);
        items.appendChild(newP);
        if(count==clicks*8-1){
            break;
        }
    }
}
req.send();
}