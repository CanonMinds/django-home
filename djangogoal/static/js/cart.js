console.log('cart js Mounted');

var updateBtns = document.getElementsByClassName('update-cart')

for(i=0;i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)

        console.log('USER:', user)
        if (user == 'AnonymousUser'){
            console.log('User is not Authenticated');
        }else{
            updateUserOrder(productId, action)
            // console.log('User is authenticated, sending data...')
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is authenticated, sending data...')

    var url = '/products/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({ 'productId':productId, 'action':action })
    })    
    .then((response) =>{
        if (!response.ok) {
            // error processing
            throw 'Error';
        }
        return response.json()
    })
    .then((data) => {
        console.log('Data:', data)
        location.reload()
    });
}