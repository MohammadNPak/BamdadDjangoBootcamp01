const like_btn = document.getElementsByClassName('like-btn')



for(let i=0;i<like_btn.length;i++){
    like_btn[i].style.backgroundColor = "yellow"
    like_btn[i].addEventListener('click',e=>{

        fetch('http://localhost:8000/api/like/post_id',{
            method:'POST'
        })
        .then(response=>{
            return {data:response.json,status:response.status}})
        .then(response_object=>{
            if (response_object.status==200){
                e.target.classList.add('btn-active')
            }
        })
    })
}





