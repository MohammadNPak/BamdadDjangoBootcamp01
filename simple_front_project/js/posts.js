const submitBtn = document.getElementById("submit-new-post")
const posts_container = document.getElementById("posts-container")
const main_container = document.getElementById("main-container")
const discussions = document.getElementsByClassName("discussion")

submitBtn.style.backgroundColor = "red";

// let posts = {
//     author:{
//             picture_url:"img/profile.jpg",
//             username:"mohammad"},
//     post:{
//         title:"first post",
//         body: `Lorem ipsum dolor, sit amet consectetur adipisicing elit.
//         Ratione dolores officia assumenda dolor maiores sint pariatur
//         quia voluptatibus voluptate perspiciatis commodi possimus nemo
//         aut, voluptas expedita facilis amet hic culpa.`,
//         date: "1401-01-01",
//         id: 1,
//         like_count : 1,
//         dislike_count: 2}}

// {credentials: "same-origin",}
// https://jsonplaceholder.typicode.com/posts


fetch("https://jsonplaceholder.typicode.com/posts", ).then(response =>{
    return response.json()
}).then(data=>{
    data.forEach(element => {
        // "userId": 1,
        // "id": 1,
        // "title"
        // "body"
        posts_container.innerHTML += `

<div class="post bg-white my-1 p-1">
<div>
    <a href="profile.html">
    <img
        class="round-img"
        src="#"
        alt=""
    />
    <h4>${element.userId}</h4>
    </a>
</div>
<div>
    <h2>${element.title}</h2>
    <p class="my-1">
        ${element.body}
    </p>
    <button class="btn">
    <i class="fas fa-thumbs-up"></i> <span>${0}</span>
    </button>
    <button class="btn">
    <i class="fas fa-thumbs-down"> <span>${0}</span></i>
    </button>
    <button href="#" class="btn btn-primary discussion">
    Discussion
    </button>
</div>
</div>
`
    });
});


Array.from(discussions).forEach(discussion=> {
 
    // a.addEventListener('click', e=>{console.log("salam")})

    discussion.addEventListener('click', e=>{
        console.log(e.sender)
        // main_container.innerHTML = `
        // <a href="posts.html" class="btn">Back To Posts</a>
        //   <div class="post bg-white p-1 my-1">
        //     <div>
        //       <a href="profile.html">
        //         <img
        //           class="round-img"
        //           src="https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50?s=200"
        //           alt=""
        //         />
        //         <h4>John Doe</h4>
        //       </a>
        //     </div>
        //     <div>
        //       <p class="my-1">
        //         Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint
        //         possimus corporis sunt necessitatibus! Minus nesciunt soluta
        //         suscipit nobis. Amet accusamus distinctio cupiditate blanditiis
        //         dolor? Illo perferendis eveniet cum cupiditate aliquam?
        //       </p>
        //     </div>
        //   </div>
    
        //   <div class="post-form">
        //     <div class="post-form-header bg-primary">
        //       <h3>Leave A Comment</h3>
        //     </div>
        //     <form class="form my-1">
        //       <textarea
        //         name="text"
        //         cols="30"
        //         rows="5"
        //         placeholder="Comment on this post"
        //       ></textarea>
        //       <input type="submit" class="btn btn-dark my-1" value="Submit" />
        //     </form>
        //   </div>
    
        //   <div class="posts">
        //     <div class="post bg-white p-1 my-1">
        //       <div>
        //         <a href="profile.html">
        //           <img
        //             class="round-img"
        //             src="https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50?s=200"
        //             alt=""
        //           />
        //           <h4>John Doe</h4>
        //         </a>
        //       </div>
        //       <div>
        //         <p class="my-1">
        //           Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint
        //           possimus corporis sunt necessitatibus! Minus nesciunt soluta
        //           suscipit nobis. Amet accusamus distinctio cupiditate blanditiis
        //           dolor? Illo perferendis eveniet cum cupiditate aliquam?
        //         </p>
        //       </div>
        //     </div>
    
        //     <div class="post bg-white p-1 my-1">
        //       <div>
        //         <a href="profile.html">
        //           <img
        //             class="round-img"
        //             src="https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50?s=200"
        //             alt=""
        //           />
        //           <h4>John Doe</h4>
        //         </a>
        //       </div>
        //       <div>
        //         <p class="my-1">
        //           Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint
        //           possimus corporis sunt necessitatibus! Minus nesciunt soluta
        //           suscipit nobis. Amet accusamus distinctio cupiditate blanditiis
        //           dolor? Illo perferendis eveniet cum cupiditate aliquam?
        //         </p>
        //       </div>
        //     </div>
        //   </div>
    
        // `
    })
});

