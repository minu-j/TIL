<template>
  <div class="border">
    <h1>이내만새컴</h1>
    <MyComponentItem 
      static-props="Mycomponent에서 보낸 데이터" 
      :dynamic-props="dynamicProps"
      @money="parentGetEvent"
      @child-input="getDynamicData"/>
  </div>
</template>

<script>
import MyComponentItem from '@/components/MyComponentItem'

export default {
    name: 'MyComponent',
    components: {
        MyComponentItem,
    },
    data: function () {
      return {
        dynamicProps: "동적인데이터",
      }
    },
    methods: {
      parentGetEvent: function (childData, c) {
        console.log(childData, c)
      },
      getDynamicData: function (i) {
        console.log(`사용자가 입력한 값은 ${i}입니다.`)
      }
    }
}
</script>

<style>
    .border {
        border: solid 1px black;
    }
</style>