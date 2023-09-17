import axiosInstance from '../axios'
import * as type from './type'

/**
 *
 * @param params 사용자 아이디, 비밀번호
 * @returns 사용자 토큰 정보
 */
const getUser = (params: type.IUserParams) => {
  return axiosInstance.get('/', { params })
}
