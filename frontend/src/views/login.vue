<template>
  <div class="app-container">
      <div class="login">
        <div class="title">用户注册/登录</div>
        <Form v-if="!go_register" ref="login" :model="loginData" :rules="rules">
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
               <Button type="primary" @click="handleRegister('login')">注册</Button>
               <Button type="primary" @click="goLogin('login')">登录</Button>
          </FormItem>
        </Form>
        <Form v-if="go_register" ref="register" :model="registerData" :rules="rules">
           <FormItem prop="user">
              <i-input type="text" v-model="registerData.user" placeholder="Username">
                  <Icon type="ios-person-outline" slot="prepend"></Icon>
              </i-input>
          </FormItem>
          <FormItem prop="mail">
              <i-input type="text" v-model="registerData.mail" placeholder="Mail">
                  <Icon type="ios-person-outline" slot="prepend"></Icon>
              </i-input>
          </FormItem>
          <FormItem prop="pwd">
              <i-input type="password" v-model="registerData.pwd" placeholder="Password">
                  <Icon type="ios-lock-outline" slot="prepend"></Icon>
              </i-input>
          </FormItem>
          <FormItem prop="pwd_confirm">
              <i-input type="password" v-model="registerData.pwd_confirm" placeholder="Confirm Password">
                  <Icon type="ios-lock-outline" slot="prepend"></Icon>
              </i-input>
          </FormItem>
          <FormItem >
              <Button type="primary" @click="goRegister('register')">注册</Button>
              <Button type="primary" @click="handleLogin()">去登录</Button>
          </FormItem>
        </Form>
      </div>
  </div>
</template>

<script>
import { login, register } from '@/api/login'
export default {
  data () {
    const validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.registerData.pwd_confirm !== '') {
          // 对第二个密码框单独验证
          this.$refs.register.validateField('pwd_confirm')
        }
        callback()
      }
    }
    const validatePassCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.registerData.pwd) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      loginData: {
        user: undefined,
        pwd: undefined
      },
      registerData: {
        user: undefined,
        mail: undefined,
        pwd: undefined,
        pwd_confirm: undefined
      },
      rules: {
        user: [
          { required: true, message: 'Please fill in the user name', trigger: 'blur' }
        ],
        pwd: [
          { required: true, message: 'Please fill in the password.', trigger: 'blur' },
          { type: 'string', min: 6, message: 'The password length can`t be less than 6 bits', trigger: 'blur' }
        ],
        mail: [
          { validator: validatePass, trigger: 'blur' }
        ],
        pwd_confirm: [
          { validator: validatePassCheck, trigger: 'blur' }
        ]
      },
      go_register: false
    }
  },
  created () {
  },
  methods: {
    handleRegister () {
      this.go_register = true
      this.$refs['login'].resetFields()
    },
    handleLogin () {
      this.go_register = false
      this.registerData.pwd = ''
      this.$refs['register'].resetFields()
    },
    goRegister (name) {
      this.$refs[name].validate((valid) => {
        if (valid) {
          register(this.registerData).then((res) => {
            console.log(res)
          })
        }
      })
    },
    goLogin (name) {
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
