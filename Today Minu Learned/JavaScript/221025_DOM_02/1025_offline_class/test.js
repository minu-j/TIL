const body = document.querySelector('body')
const obj = {
    logThis: function logThis() {
        console.log(this)
    },
    setTime: function () {
        setTimeout(this.logThis, 2000)
    },
    addEvent: function () {
        body.addEventListener('click', this.logThis)
    }
}

obj.logThis()
obj.setTime()
obj.addEvent()