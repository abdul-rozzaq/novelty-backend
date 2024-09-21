const modalButtons = document.querySelectorAll('.modal-button');
const wrappers = document.querySelectorAll('.modal-wrapper')
const closeButton = document.querySelectorAll('.close-button');

const switchBlockScroll = () => {
    if (document.body.classList.contains('block-scroll')) {
        document.body.classList.remove('block-scroll');
    } else {
        document.body.classList.add('block-scroll');
    }
}

modalButtons.forEach(btn => {
    console.log(btn);

    btn.addEventListener('click', (e) => {
        const modalId = e.target.getAttribute('data-target-id');
        const modal = document.querySelector(`[data-id="${modalId}"]`);

        modal.classList.add('show');
        
        switchBlockScroll()
    })
});


wrappers.forEach(element => {
    element.addEventListener('click', (e) => {
        const target = e.target
        const modal = element.querySelector('.modal')

        if (target == element) {
            element.classList.remove('show');

            switchBlockScroll();
        }
    })
}); 


closeButton.forEach(btn => {
    btn.addEventListener('click', (e) => {
        btn.parentElement.parentElement.classList.remove('show');

        switchBlockScroll();
    })
});


// let modalWrappers = document.querySelectorAll('.modal-wrapper');