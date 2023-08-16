// to fetch API in frontend, you can use the following:
// XMLHttpRequest
// Axios
// Fetch Request

// read more on how to fetch www.developer.mozillar.org

//to test this, we go to reqres.in https://reqres.in/api/users/2

let accountNumber = "0110302460"
let bank = "032"

const xhr = new XMLHttpRequest()
xhr.open("GET", `https://api.paystack.co/bank/resolve?account_number=${accountNumber}&bank_code=${bank}`)
//xhr.open("GET","https://api.paystack.co/bank")
xhr.setRequestHeader("Authorization", "Bearer sk_test_eeb9889b80e751a8f2653c975744c9811c3dbeab")
xhr.send()
xhr.onload = function(){
    try{
       // let res = JSON.parse(xhr.respomse).data
        let {account_name } = JSON.parse(xhr.response).data
        console.log("Account Name", account_name)
    }catch(error){
        console.log(error)
    }
}
// xhr.onload = function()

// {
//     if(xhr.status === 200){
//         console.log(xhr.response)
//     }else{
//         console.log(xhr.status)
//     } 
// }
// const xhr = new XMLHttpRequest()
// xhr.open("GET", "https://api.paystack.co/bank/resolve?account_number=0001234567&bank_code=058")
// xhr.setRequestHeader("Authotization", "Bearer sk_test_eeb9889b80e751a8f2653c975744c9811c3dbeab")
// xhr.send()
// xhr.onload = function(){
//     if(xhr.status === 200){

//         // let x = [2, 4, 5, "hello", 20]

//         // let {first, second, third} = x

//         // const data = JSON.parse(xhr.response).data
//         // const {email, first_name, last_name} = data

//         const {email, first_name, last_name} = JSON.parse(xhr.response).data
//         console.log("Email", email)
//         console.log("Firstname", first_name)
//         console.log("Lastname", last_name)
        
//         //const newOb = {a: "hello", b: spread}
//         console.log(JSON.stringify(newOb))
//        // console.log(xhr.responseText)
//     }else{
//         console.log(xhr.status)
//     } 
// }


// import axios from "axios";

// const response = axios.get("https://reqres.in/api/users/2")



// PROMISE\


function func(resolve, rejectr){
    setTimeout(() => {console.log("Im the setTimeout function")
    resolve("Resolving...")
},2000)
}

function callBack(value){
    console.log("In the callback function")
    console.log(value)
}

let promise = new Promise(func)
promise.then(callBack)


function add(resolve, reject){
    if(true){
        resolve(1)
    }
    
}



// Promise & Promise chainning - Article [Assignment]
