<template>
     <div class="layout">
        <div class="header">
            <div class="title">我的博客</div>
            <div class="login" @click="login">登录</div>
        </div>
    </div>
</template>

<script>
export default {
  methods: {
    login () {
      this.$router.push('/login')
    }
  }
}
</script>

<style scope lang="scss">
.header{
    width: 100%;
    height: 50px;
    background-color:deepskyblue;
    display: flex;
    justify-content: space-between;
    align-items:center;
    .title{
        color: #fff;
        margin-left: 20px;
        font-size: 24px;
    }
    .login{
        color: #fff;
        vertical-align: middle;
        width: 30px;
        margin-right:20px;
        cursor:pointer
    }
}
</style>
