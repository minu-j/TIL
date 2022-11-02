<template>
  <div>
    <h3>컴포넌트 하위~</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">클릭</button>
    <input 
      v-model="childInputData" 
      type="text"
      @keyup.enter="childInput"  
    >
  </div>
</template>

<script>
export default {
    name: 'MyComponentItem',
    props: {
      staticProps: String,
      dynamicProps: String,
    },
    data: function () {
      return {
        childInputData: null,
      }
    },
    methods: {
      childToParent: function () {
        this.$emit('money', '자식이 보낸 데이터', '2222')
      },
      childInput: function () {
        this.$emit('child-input', this.childInputData)
        this.childInputData = null
      }
    }
}
</script>

<style>

</style>