import { useEffect, useState } from 'react'
import { Producto } from './types'

function App() {
  const [productos, setProductos] = useState<Producto[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/productos/')
      .then(response => response.json())
      .then(data => {
        setProductos(data)
        setLoading(false)
      })
      .catch(error => console.error('Error fetching productos:', error))
  }, [])

  if (loading) return <div class="p-10 text-center">Cargando inventario...</div>

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-indigo-700 mb-8">Inventario (React + Django)</h1>
        
        <div className="grid gap-4">
          {productos.map(p => (
            <div key={p.id} className="bg-white p-6 rounded-xl shadow-sm border border-gray-200 flex justify-between items-center">
              <div>
                <h2 className="text-xl font-semibold">{p.nombre}</h2>
                <p className="text-indigo-500 font-mono text-sm">{p.SKU}</p>
              </div>
              <div className="text-right">
                <span className="text-2xl font-bold text-gray-800">{p.cantidad}</span>
                <p className="text-xs text-gray-400 uppercase">Unidades</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default App