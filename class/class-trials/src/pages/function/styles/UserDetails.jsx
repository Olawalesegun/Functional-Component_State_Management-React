import { useReducer } from 'react'
import { useState } from 'react'
import React from 'react'
import { UserDetailContain, TextContain, InputStyle } from './UserDetailsStyles'
import { useReducer } from 'react'

  // USEREDUCER
  function reducer(state, action) {
    switch (action.type) {
        case "handleChange":
            return {
                ...state,
                [action.field]: action.payload
            }

            default:
                break;
    }
  }

function UserDetails() {
    const initialValue = {
        firstName: '',
        lastName: '',
        email: '',
        age: 0,
        height: 0.0,
        userName: ''
    }

    const [data, dispatch] = useReducer(reducer, initialValue)

    const handleChange = (event) => {
        dispatch({
            type: "handleChange",
            field: event.target.name,
            payload: event.target.value
        })
    }

    const handleButton = (event) => {
        console.log("I got here")
        dispatch({
            type: "handleButtonText",
            field: event.target.name,
            payload: " Hello"
        })
    }
    // USESTATE Functional component state mgt
    // const [data, setData] = useState(initialValue)

    // const handleChange = (event) => {
    //     setData((prevState) => ({
    //         ...prevState, 
    //         [event.target.name]: event.target.value
    //     }))
    // }

  

    return (
        <UserDetailContain>
            <UserDetailContain>
                <TextContain>FirstName: {data.firstName}</TextContain> 
                <TextContain>LastName: {data.lastName}</TextContain>
               <TextContain> UserName: {data.userName}</TextContain>
                <TextContain>Email: {data.email}</TextContain>
                <TextContain>Age: {data.age}</TextContain>
              <TextContain>Height: {data.height}</TextContain>
              <ButtonStyle name='buttonText' onClick={handleButtonText}>{data.buttonText}</ButtonStyle>/>
            </UserDetailContain>
            <InputStyle value={data.firstName} name={"firstName"} type='text' onChange={handleChange} />
            <InputStyle value={data.lastName} name={"lastName"} type='text' onChange={handleChange} />
            <InputStyle value={data.userName} name={"userName"} type='text' onChange={handleChange} />
            <InputStyle value={data.email} name={"email"} type='email' onChange={handleChange} />
            <InputStyle value={data.age} name={"age"} type='number' onChange={handleChange} />
            <InputStyle value={data.height} name={"height"} type='number' onChange={handleChange} />
        </UserDetailContain>
        
    )
}

export default UserDetails