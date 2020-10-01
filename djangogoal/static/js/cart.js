console.log('Cart js Mounted');

var updateBtns = document.getElementsByClassName('update-cart')

for(i=0;i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var ordername = this.dataset.name

        
        if (user == 'AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            updateUserOrder(productId, action)
            document.getElementById('orderupdate-status').classList.remove('hidden')
            document.getElementById('orderupdate-status').innerHTML = ordername + ' was now added to your orders';
            setTimeout(function(){ location.reload(); }, 5000);
        }
    })
}


var arrowupBtns = document.getElementsByClassName('add-cart')

for(i=0;i<arrowupBtns.length; i++){
    arrowupBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var ordername = this.dataset.name

        if (user == 'AnonymousUser'){
            alert('Adding item')
            addCookieItem(productId, action)
        }else{
            updateUserOrder(productId, action)
        }
    })
}

var arrowdownBtns = document.getElementsByClassName('subtract-cart')

for(i=0;i<arrowdownBtns.length; i++){
    arrowdownBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var ordername = this.dataset.name

        if (user == 'AnonymousUser'){
            alert('Removing item')
            addCookieItem(productId, action)
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function addCookieItem(productId, action){
    console.log('User not logged in..');
    if (action == 'add'){
        if (cart[productId] == undefined){
        cart[productId] = {'quantity':1}
        }else{
            cart[productId]['quantity'] + 1
        }
    }

    if (action == 'remove'){
        cart[productId]['quantity'] -= 1

        if (cart[productId]['quantity'] <= 0){
            console.log('Remove item')
            delete cart[productId]
        }
    }

    console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
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
