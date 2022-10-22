<template>
  <n-config-provider :theme="theme">
    <n-message-provider ref="messageProvider">
      <n-layout>
        <n-layout-header
          style="height: 72px; padding: 12px; display: flex"
          bordered
        >
          <n-text class="ui-logo">
            <img
              src="./assets/suav.png"
              style="height: 48px; margin-right: 64px"
            />
          </n-text>
          <div style="display: flex; align-items: center">
            <n-menu mode="horizontal" :options="menuOptions" />
          </div>
        </n-layout-header>
        <n-layout-content style="min-height: calc(100vh - 72px); display: flex; flex-direction: column;">
          <router-view />
        </n-layout-content>
      </n-layout>
    </n-message-provider>
  </n-config-provider>
</template>

<script>
import { h } from "vue";
import { RouterLink } from "vue-router";
import { darkTheme } from "naive-ui";

export default {
  name: "App",
  components: {},
  data() {
    return {
      theme: darkTheme,
      menuOptions: [
        {
          label: () =>
            h(
              RouterLink,
              {
                to: {
                  name: "image",
                },
              },
              { default: () => "Image" }
            ),
          key: "route-image",
          //icon: renderIcon(HomeIcon),
        },
        {
          label: () =>
            h(
              RouterLink,
              {
                to: {
                  name: "map",
                },
              },
              { default: () => "Map" }
            ),
          key: "route-Map",
          //icon: renderIcon(HomeIcon),
        },
      ],
    };
  },
};
</script>

<style>
.ui-logo {
  cursor: pointer;
  display: flex;
  align-items: center;
}
html, body, #app {
  height: 100%
}
</style>
