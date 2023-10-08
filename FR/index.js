import React from "react";
import ReactDOM from "react-dom";

// DECLARATIVE --- What should be done, you do not need to explain how it should be done as program i s expected to take care of that!
function MainHeader() {
  return <h1> I'm learning React!!!</h1>;
}

ReactDOM.render(
  <div>
    <MainHeader />
  </div>,
  document.getElementById("root")
);

// IMPERATIVE --- how should it be done (step by step)!
const h1 = document.createElement("h1");
h1.textContent = "This is an imperative approach or way to program";
h1.className = "header";
document.getElementById("root").append(h1);

// JSX
const h1 = document.createElement("h1");
h1.textContent = "Hello world";
h1.className = "header";
console.log(h1); // <h1 class="header">

const element = <h1 className="header"> This is JSX</h1>;
console.log(element);

/*{
    type: "h1", key:null, ref: null, props: {className: "header", children: "This is JSX"},
    _owner: null,
    _store: {}
}*/

// CHALLENGE:
/*create a navBar in JSX: 
        use the semantic nav elements as the parent wrapper
        Have an h1 element with the brand name of your "website"
        insert an unordered list for  the other nav elements
        - Inside the `ul`, have three `li`s for "Pricing",
            "About", and "Contact"
        - Don't worry about styling yet - it'll just be plain-looking HTML for now
    */

const navBar = (
  <nav>
    <h1> Bob's Bistro</h1>
    <ul>
      <li>Menu</li>
      <li>About</li>
      <li>Contact</li>
    </ul>
  </nav>
);

ReactDOM.render(navBar, document.getElementById("root"));

// JSX returns plain Json object and here is a proof
const page = (
  <section>
    <h1> My awesome website in react</h1>
    <h3> Reasons I love React</h3>
    <ol>
      <li> It's composable </li>
      <li> It's declarative</li>
      <li> It's a hirable skill</li>
      <li> It's actively maintained by skilled people</li>
    </ol>
  </section>
);

document.getElementById("root").append(page);
// The above will return [object object]; to solve this, that is to access the entries in the objects

document.getElementById("root").append(JSON.stringify(page));
// The above as a solution to the [object object] returned will help
// to decipher the contents of the object, that is it will return a JSON repsonse
// containing Keys and values. However, thats not what we want, so to solve this, we do;

ReactDOM.render(page, document.getElementById("root"));

// USING function to create custom components

//RULES
// 1. Always give function the the paschal case naming convention instead of camelCase  NamingConvention
// 2. instead of calling the function with parameters as we are used to, we will wrpa itr in a tag

function CreatingCustomeComponent() {
  return (
    <div>
      {" "}
      My awesome website
      <h1>My awesome website</h1>
      <h3> Reasons I love React</h3>
      <ol>
        <li>Composable</li>
        <li>Declarative</li>
      </ol>
    </div>
  );
}

ReactDOM.render(<CreatingCustomeComponent />, document.getElementById("root"));
 

function Page(){
    return (
       <div>
         <h1>Names of Food in Ypruba Dialect</h1>
        <ol>
            <li> EBA</li>
            <li> EWA AGOYIN</li>
            <li> MOI_MOI ALATA</li>
        </ol>
       </div> 
    )
}
ReactDOM.render(<Page/>, document.getElementById("root"))
