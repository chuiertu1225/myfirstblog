<template>
  <div class="app-container">
      <div class="login">
        <div class="title">用户注册/登录</div>
        <Form ref="login" :model="loginData" :rules="rules">
          <FormItem prop="user">
                <i-input type="text" v-model="loginData.user" placeholder="Username/Email">
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                </i-input>
          </FormItem>
          <FormItem prop="pwd">
                <i-input type="password" v-model="loginData.pwd" placeholder="Password">
                    <Icon type="ios-lock-outline" slot="prepend"></Icon>
                </i-input>
          </FormItem>
           <FormItem >
               <Button type="primary" @click="handleSubmit('login')">注册</Button>
               <Button type="primary" @click="handleSubmit('login')">登录</Button>
          </FormItem>
        </Form>
      </div>

  </div>
</template>

<script>
import {login} from '@/api/login'
export default {
  data () {
    return {
      loginData: {
        user: undefined,
        pwd: undefined
      },
      rules: {
        user: [
          { required: true, message: 'Please fill in the user name', trigger: 'blur' }
        ],
        pwd: [
          { required: true, message: 'Please fill in the password.', trigger: 'blur' }
          // { type: 'string', min: 6, message: 'The password length can`t be less than 6 bits', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    handleSubmit (name) {
      this.$refs[name].validate((valid) => {
        if (valid) {
          login(this.loginData).then((res) => {
            console.log(res)
            this.$Message.success('Success!')
          })
        } else {
          this.$Message.error('Fail!')
        }
      })
    }
  }
}
</script>

<style scope lang="scss">
.app-container{
    background-color: #fafafa;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    .login{
        background-color:#def4f3;
        width: 300px;
        height:500px;
        .title{
            width: 130px;
            margin-top:50px;
            margin-left:90px;
            color: #999;
            font-size:18px;
        }
        .ivu-form{
            padding-top: 100px;
            padding-left: 10px;
            padding-right: 10px;
            height: 100%;
            .ivu-form-item{
                .ivu-form-item-content{
                    text-align: center
                }
            }
        }
    }
}

</style>
