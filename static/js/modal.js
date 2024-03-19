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



// ======================================================== //


const imageFields = document.querySelectorAll('.image-field')

imageFields.forEach(field => {
    const input = field.querySelector('input[type="file"]')
    
    field.addEventListener('click', () => {
        input.click();
    })

    input.addEventListener('change', () => {
        console.log(input.files);
        console.log(input.files.length);

        const files = [...input.files].slice(0, 6)
        const boxes = field.querySelectorAll('div.image')

        console.log(boxes);

        for (const box of boxes) {
            box.innerHTML = ''
        }        


        for (let index = 0; index < files.length; index++) {
            const file = files[index]
            const box = boxes[index]

            const fileReader = new FileReader();

            fileReader.onload = () => {
                let image = document.createElement('img')

                image.src = fileReader.result
                
                while (box.firstChild) {
                    box.firstChild.remove()
                }
                
                box.appendChild(image)
            }

            fileReader.readAsDataURL(file);            
        }
    })
})



// let modalWrappers = document.querySelectorAll('.modal-wrapper');