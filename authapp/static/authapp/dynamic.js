// this function is for closing the alert block 
document.addEventListener('DOMContentLoaded', function(){
    const closeButtons = document.querySelectorAll('.close-btn');
    closeButtons.forEach(function(btn){
        btn.addEventListener('click',function(event){
            const msgBlock = btn.closest('.message');
            if(msgBlock){
                const displayValue = window.getComputedStyle(msgBlock).display;
                if(displayValue === 'flex'){
                    msgBlock.style.display = 'none'
                }
            }
        });
    });
});