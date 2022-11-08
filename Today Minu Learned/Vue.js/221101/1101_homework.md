1. `True`, `True`, `False`

2. method는 화면 출력시마다 계산하지만, computed는 여러번 출력 시 한번만 계산하고, 값이 저장되어 출력된다.

3. ```html
    <body>
        <div id="app">
            <div v-for="(num, index) in oddNumbers" :key="index">
            <p>{{ num }}</p>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
        <script>
            const app = new Vue({
            el: '#app',
            data: {
                nums: [1, 2, 3, 4, 5, 6]
            },
            computed: {
                oddNumbers: function () {
                    const this.nums.filter{(num) => {
                        return num % 2 == 1
                        }}
                    }
                }
            })
        </script>
    </body>
    ```