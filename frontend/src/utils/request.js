import axios from 'axios'
import router from '../router'
// import { MessageBox, Message } from 'element-ui'
// import store from '@/store'
// import { getToken } from '@/utils/auth'
// import Cookies from 'js-cookie'

// create an axios instance
const service = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  // withCredentials: true, send cookies when cross-domain requests
  timeout: 5000 // request timeout
})

// request interceptor
service.interceptors.request.use(
  config => {
    // do something before request is sent

    // if (config.hasOwnProperty('params')) {
    //   if (config.params.hasOwnProperty('page') & config.params.hasOwnProperty('limit')) {
    //     config['params']['offset'] = (config['params']['page'] - 1) * config['params']['limit']
    //   }
    // }

    // if (process.env.NODE_ENV === 'development') {
    //   config.headers['flag'] = Cookies.get('flag') || 'caiwu'
    // } else {
    //   config.headers['flag'] = window.location.host.split('.')[0]
    // }

    // if (store.getters.token) {
    // let each request carry token
    // ['X-Token'] is a custom headers key
    // please modify it according to the actual situation
    //   config.headers['Token'] = getToken()
    // }

    return config
  },
  error => {
    // do something with request error
    console.log(error) // for debug
    return Promise.reject(error)
  }
)

// response interceptor
service.interceptors.response.use(
  /**
     * If you want to get http information such as headers or status
     * Please return  response => response
     */

  /**
     * Determine the request status by custom code
     * Here is just an example
     * You can also judge the status by HTTP Status Code
     */
  response => {
    const res = response.data
    // if the custom code is not 20000, it is judged as an error.
    // code小于40000认为是成功的请求
    if (res.code >= 40000) {
      // 50008: Illegal token; 50012: Other clients logged in; 50014: Token expired;
      if (res.code === 40404) {
        router.push({ path: '/404' })
      } else if (res.code === 61000 || res.code === 61001 || res.code === 61002 || res.code === 61003 || res.code === 61004) {
        this.$Modal.confirm({
          title: 'RELOG',
          content: res.msg + '确认登录',
          onOk: () => {
            this.$Message.info('Clicked ok')
          },
          onCancel: () => {
            this.$Message.info('Clicked cancel')
          }
        })
        // to re-login
        // MessageBox.confirm(res.msg, '确认登录', {
        //   confirmButtonText: '重新登录',
        //   cancelButtonText: '取消',
        //   type: 'warning'
        // }).then(() => {
        //   store.dispatch('user/resetToken').then(() => {
        //     location.reload()
        //   })
        // }).catch(() => {})
      } else {
        // Message({
        //   message: res.msg || '网络错误',
        //   type: 'error',
        //   duration: 5 * 1000
        // })
        this.$Message.error({
          content: res.msg || '网络错误',
          during: 5
        })
        return Promise.reject(res)
      }
      return Promise.reject(res)
    } else {
      return res
    }
  },
  error => {
    console.log('err: ' + error) // for debug
    // 403都规定为用户没有访问权限
    if (error.message.trim().endsWith('403')) { error.message = '没有访问权限' }
    this.$Message.error({
      content: error.msg || '网络错误',
      during: 5
    })
    return Promise.reject(error)
  }
)

export default service
