import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

const page = (name) => () => import('@/views/' + name)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    {
      path: '/',
      name: 'Main',
      component: page('main'),
      meta: {
        title: '首页'
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: page('login'),
      meta: {
        title: '登录'
      }
    }

  ]
})
