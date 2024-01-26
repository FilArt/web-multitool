import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("@/components/HomeView.vue"),
  },
  {
    path: "/url-shortener",
    meta: {
      title: "URL Shortener",
    },
    component: () => import("@/components/UrlShortener.vue"),
  },
];

export default createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHashHistory(),
  routes,
});
