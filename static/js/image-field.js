
const imageFields = document.querySelectorAll('.image-field')

imageFields.forEach(field => {
    const input = field.querySelector('input[type="file"]')
    
    field.addEventListener('click', () => {
        input.click();
    })

    input.addEventListener('change', () => {

        const files = [...input.files].slice(0, 6)
        const boxes = field.querySelectorAll('div.image')

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

