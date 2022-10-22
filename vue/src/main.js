import { createApp } from 'vue'
import {
    create,
    NButton,
    NLayout,
    NLayoutHeader,
    NLayoutContent,
    NConfigProvider,
    NMessageProvider,
    NH1,
    NText,
    NMenu,
    NLayoutSider,
    NList,
    NListItem,
    NScrollbar,
} from 'naive-ui'

import App from './App.vue'
import router from './router'

const naive = create({
    components: [
        NButton,
        NLayout,
        NLayoutHeader,
        NLayoutContent,
        NConfigProvider,
        NMessageProvider,
        NH1,
        NText,
        NMenu,
        NLayoutSider,
        NList,
        NListItem,
        NScrollbar,
    ]
})

const app = createApp(App)
app.use(router)
app.use(naive)
app.mount('#app')