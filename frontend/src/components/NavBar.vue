<template>
  <Disclosure as="nav" class="bg-blue min-h-full" v-slot="{ open }">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="relative flex h-16 items-center justify-between">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
          <!-- Mobile menu button-->
          <DisclosureButton
            class="inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 bg-cornsilk hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
          >
            <span class="sr-only">Open main menu</span>
            <Bars3Icon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
            <XMarkIcon v-else class="block h-6 w-6" aria-hidden="true" />
          </DisclosureButton>
        </div>
        <div
          class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start"
        >
          <div class="flex flex-shrink-0 items-center">
            <img
              class="block h-8 w-auto lg:hidden"
              src="../assets/prismnavbar.svg"
            />
            <img
              class="hidden h-8 w-auto lg:block"
              src="../assets/prismnavbar.svg"
            />
          </div>
          <div class="hidden sm:ml-6 sm:block">
            <div class="flex space-x-4">
              <router-link to="/dashboard">
                <button
                  class="text-cornsilk hover:darkblue px-3 py-2 rounded-md text-sm font-medium"
                  :class="{ 'bg-darkblue': getActiveTab('/dashboard') }"
                >
                  Dashboard
                </button>
              </router-link>
              <!-- <router-link to="/survey">
                <button
                  class="hover:darkblue text-cornsilk px-3 py-2 rounded-md text-sm font-medium"
                  :class="{ 'bg-darkblue': getActiveTab('/survey') }"
                >
                  Survey
                </button>
              </router-link> -->
              <!-- <router-link to="/result">
                <button
                  class="text-cornsilk hover:darkblue px-3 py-2 rounded-md text-sm font-medium"
                  :class="{ 'bg-darkblue': getActiveTab('/result') }"
                >
                  Result
                </button>
              </router-link> -->
              <!-- <router-link to="/info">
                <button
                  class="text-cornsilk hover:darkblue px-3 py-2 rounded-md text-sm font-medium"
                  :class="{ 'bg-darkblue': getActiveTab('/info') }"
                >
                  Information
                </button>
              </router-link> -->
            </div>
          </div>
        </div>
        <div
          v-if="isAuthenticated"
          class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0"
        >
          <!-- Profile dropdown -->
          <Menu as="div" class="relative ml-3">
            <div>
              <MenuButton
                class="flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
              >
                <img
                  class="h-8 w-8 rounded-full"
                  src="../assets/stockphoto.jpg"
                  alt=""
                />
              </MenuButton>
            </div>
            <transition
              enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <MenuItems
                class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
              >
                <MenuItem
                  v-slot="{ active }"
                  @click="($event) => router.push('/profile')"
                >
                  <a
                    href="#"
                    :class="[
                      active ? 'bg-gray-100' : '',
                      'block px-4 py-2 text-sm text-gray-700',
                    ]"
                    >Your Profile</a
                  >
                </MenuItem>
                <!-- <MenuItem v-slot="{ active }">
                  <a
                    href="#"
                    :class="[
                      active ? 'bg-gray-100' : '',
                      'block px-4 py-2 text-sm text-gray-700',
                    ]"
                    >Settings</a
                  >
                </MenuItem> -->
                <MenuItem v-slot="{ active }" @click="logout()">
                  <a
                    href="#"
                    :class="[
                      active ? 'bg-gray-100' : '',
                      'block px-4 py-2 text-sm text-gray-700',
                    ]"
                    >Sign out</a
                  >
                </MenuItem>
              </MenuItems>
            </transition>
          </Menu>
        </div>
      </div>
    </div>

    <DisclosurePanel class="sm:hidden">
      <div class="space-y-1 px-2 pt-2 pb-3">
        <router-link to="/dashboard">
          <DisclosureButton
            class="w-full text-gray-800 hover:bg-gray-300 mb-1 px-3 py-2 rounded-md text-sm font-medium"
            :class="{ 'bg-cornsilk': getActiveTab('/dashboard') }"
          >
            Dashboard
          </DisclosureButton>
        </router-link>
        <!-- <router-link to="/survey">
          <DisclosureButton
            class="w-full hover:bg-gray-300 text-gray-800 mb-1 px-3 py-2 rounded-md text-sm font-medium"
            :class="{ 'bg-cornsilk': getActiveTab('/survey') }"
          >
            Survey
          </DisclosureButton>
        </router-link> -->
        <!-- <router-link to="/result">
          <DisclosureButton
            class="w-full text-gray-800 hover:bg-gray-300 mb-1 px-3 py-2 rounded-md text-sm font-medium"
            :class="{ 'bg-cornsilk': getActiveTab('/result') }"
          >
            Result
          </DisclosureButton>
        </router-link> -->
        <!-- <router-link to="/info">
          <DisclosureButton
            class="w-full text-gray-800 hover:bg-gray-300 px-3 py-2 rounded-md text-sm font-medium"
            :class="{ 'bg-cornsilk': getActiveTab('/info') }"
          >
            Information
          </DisclosureButton>
        </router-link> -->
      </div>
    </DisclosurePanel>
  </Disclosure>
</template>
<script setup>
/* eslint-disable */
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
} from "@headlessui/vue";

import { Bars3Icon, BellIcon, XMarkIcon } from "@heroicons/vue/24/outline";
import { router } from "../main.js";
import { logout } from "../../Logic/authentication.js";
import { ref } from "vue";
import { ROUTES } from "../constant/routes.js";
import { storeToRefs } from "pinia";
import { userStateStore } from "../store/userstate.js";
import { check_authen } from "../../Logic/authentication.js";

check_authen();

const { isAuthenticated } = storeToRefs(userStateStore());
function getActiveTab(value) {
  const path = router?.currentRoute?.value?.path;
  if (value === path) {
    return true;
  } else {
    return false;
  }
}
</script>
