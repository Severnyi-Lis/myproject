let cart = {
    'aglaonema_pl' : 2
}

document.onclick = event => {
    if(event.target.classList.contains('plus')) {
        plusFunnction(event.target.dataset.id)
    }
    if(event.target.classList.contains('minus')) {
        minusFunnction(event.target.dataset.id)
    }
}

const plusFunnction = id =>{ //увеличение товара
    cart[id]++;
    renderCart();
}

const minusFunnction = id =>{ //уменьшение товара
    if (cart[id]-1 ==0){
        deletFunction(id)
        return true;
    }
    cart[id]--;
    renderCart();
}

const deletFunction = id =>{ //удаление товара 
    delete cart[id];
    renderCart();
}

const renderCart = () => {
    console.log(cart);
}

renderCart();