import { API_URL } from '@lib/Enviroments'

export const GetAllProducts = async (preferencia_id) => {
  let query_params = new URLSearchParams()
  if (preferencia_id) {
    query_params.append('preferencia', preferencia_id)
  }
  //const response = await fetch(`${API_URL}/productos/productos/list?${query_params}`)
  const response = await fetch(`${API_URL}/producto`)
  const data = await response.json()
  console.log(data);
  return data
}

export const GetProductById = async (id) => {
  const response = await fetch(`${API_URL}/productos/productos/${id}`)
  const data = await response.json()
  return data
}

export const PostProduct = async (product) => {
  const response = await fetch(`${API_URL}/producto`, {
    method: 'POST',
    headers: {
      "Content-Type": "multipart/form-data",
      "Accept": "application/json",
      "type": "formData"
    },
    body: JSON.stringify(product)
  })
  const data = await response.json()
  return data
}
