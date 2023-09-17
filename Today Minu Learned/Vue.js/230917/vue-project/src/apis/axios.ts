import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: '',
  timeout: 3000
})

axiosInstance.interceptors.request.use((config) => {
  return config
})

axiosInstance.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    return error
  }
)

export default axiosInstance
