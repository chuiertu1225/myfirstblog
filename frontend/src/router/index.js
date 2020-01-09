import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

const page = (name) => () => import('@/views/' + name)

const routes = [
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

const router = new Router({
  routes
})

// router.beforeEach((to, from, next) => {
//   console.log(222)
//   next()
// })
export default router
