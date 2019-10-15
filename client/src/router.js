import Vue from 'vue';
import Router from 'vue-router';
import Urls from './components/Urls.vue';
import Ping from './components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Urls',
      component: Urls,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
