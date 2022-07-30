<script setup>
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>Documentation</template>
    Documentation about the impletmenation can be found on our github.
    <a href="https://github.com/foximler/natHacks-2022" target="_blank">natHacks-2022</a>
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>Hardware</template>

    This project was trained and designed to interface with EPOC BCI interfaces. The software itself is designed to not be resource intensive and as such can run on as little as a raspberry pi 4. This brings the total cost of implementing this project to roughly $1000 per complete setup. 
  </WelcomeItem>



  <WelcomeItem>
    <template #icon>
      <SupportIcon />
    </template>
    <template #heading>Support Us</template>

    As an hackathon project we don't expect to get much from this. To help us out consider raising our clout by following us on github. 
    <a target="_blank" href="https://github.com/foximler/">Fox Imler</a> or 
    <a target="_blank" href="https://github.com/alexciok">Alex Ciok</a>. Better yet you can connect with us on linked in: <a target="_blank" href="https://www.linkedin.com/in/foximler/">Fox Imler</a> and <a target="_blank" href="https://www.linkedin.com/in/alex-ciok-796015164/">Alex Ciok</a> .
  </WelcomeItem>
</template>
