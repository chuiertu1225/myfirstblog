<template>
  <div class="app-container">
      <div class="login">
        <div class="title">用户{{go_register?'注册':'登录'}}</div>
        <transition name="fade-left">
          <Form v-if="!go_register" ref="login" :model="loginData" :rules="rules" key="1">
            <FormItem prop="user">
                <i-input type="text" v-model="loginData.user" placeholder="Username/Email">
                      <Icon type="ios-person-outline" slot="prefix"></Icon>
                </i-input>
            </FormItem>
            <FormItem prop="pwd">
                <i-input type="password" v-model="loginData.pwd" placeholder="Password">
                      <Icon type="ios-lock-outline" slot="prefix"></Icon>
                </i-input>
            </FormItem>
            <FormItem >
                <Button type="primary" @click="handleRegister('login')">去注册</Button>
                <Button type="primary" @click="goLogin('login')">登录</Button>
            </FormItem>
          </Form>
          <Form v-if="go_register" ref="register" :model="registerData" :rules="rules" key="2">
            <FormItem prop="username">
                <i-input type="text" v-model="registerData.username" placeholder="Username">
                    <Icon type="ios-person-outline" slot="prefix"></Icon>
                </i-input>
            </FormItem>
            <FormItem prop="email">
                <i-input type="text" v-model="registerData.email" placeholder="Mail">
                    <Icon type="ios-mail-outline" slot="prefix"></Icon>
                </i-input>
            </FormItem>
            <FormItem prop="password">
                <i-input type="password" v-model="registerData.password" placeholder="Password">
                    <Icon type="ios-lock-outline" slot="prefix"></Icon>
                </i-input>
            </FormItem>
            <FormItem prop="password_confirm">
                <i-input type="password" v-model="registerData.password_confirm" placeholder="Confirm Password">
                    <Icon type="ios-lock-outline" slot="prefix"></Icon>
                </i-input>
            </FormItem>
            <FormItem >
                <Button type="primary" @click="goRegister('register')">注册</Button>
                <Button type="primary" @click="handleLogin()">去登录</Button>
            </FormItem>
          </Form>
        </transition>
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
        if (this.registerData.password_confirm !== '') {
          // 对第二个密码框单独验证
          this.$refs.register.validateField('password_confirm')
        }
        callback()
      }
    }
    const validatePassCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.registerData.password) {
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
        username: undefined,
        email: undefined,
        password: undefined,
        password_confirm: undefined
      },
      rules: {
        user: [
          { required: true, message: 'Please fill in the user name', trigger: 'blur' }
        ],
        username: [
          { required: true, message: 'Please fill in the user name', trigger: 'blur' }
        ],
        pwd: [
          { required: true, message: 'Please fill in the password.', trigger: 'blur' },
          { type: 'string', min: 6, message: 'The password length can`t be less than 6 bits', trigger: 'blur' }
        ],
        email: [
          { validator: validatePass, trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Please fill in the password.', trigger: 'blur' },
          { type: 'string', min: 6, message: 'The password length can`t be less than 6 bits', trigger: 'blur' }
        ],
        password_confirm: [
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
@import '@/styles/index.scss';
html {
    overflow: -moz-hidden-unscrollable;
    height: 100%;
}

body::-webkit-scrollbar {
    display: none;
}

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
            margin-left:110px;
            color: #999;
            font-size:18px;
        }
        .ivu-form{
            padding-top: 80px;
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
