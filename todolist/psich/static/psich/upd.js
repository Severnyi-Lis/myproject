window.addEventListener(
    'load',
  //  () => {
        new_update//();
  //  }
)
function new_update() {
    console.log(my_name.value)
    fetch('/psicholog/',{
        method:'post',
        headers: {
            'X-CSRFToken': document.querySelector(
                '[name=csrfmiddlewaretoken]').value
        }})
    .then((value) =>{
        if(value.status === 200){
            console.log(value)
        }
        else{
            console.log(value.statusText);
            console.log(value.status)
        }
    })
}

