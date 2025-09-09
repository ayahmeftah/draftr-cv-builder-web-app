function init() {
    const currentCheckboxElem = document.querySelector('#is_current')
    const endDateInputElem = document.querySelector('#end_date')

    function endDateDisable() {
        if (this.checked) {
            endDateInputElem.disabled = true
            endDateInputElem.value = ''
        } else {
            endDateInputElem.disabled = false
        }
    }

    currentCheckboxElem.addEventListener('change', endDateDisable)

    currentCheckboxElem.dispatchEvent(new Event('change'))
}

document.addEventListener('DOMContentLoaded',init)