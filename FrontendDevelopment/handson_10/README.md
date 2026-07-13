# Hands-On 10
## API Integration & Advanced State Management

### Framework Used
Vue 3 + Pinia + Axios

### Features Implemented

- Centralised Axios API Layer
- Request Interceptor
- Response Interceptor
- Pinia Store
- fetchAndEnroll()
- storeToRefs()
- $reset()
- Global Error Handler
- Vue Router

---

## State Management Comparison

### React + Redux Toolkit

- Uses Redux Store
- Uses createAsyncThunk for API calls
- More boilerplate
- Good for large applications

### Angular + NgRx

- Uses Actions
- Reducers
- Effects
- Selectors
- Most structured approach

Flow:

Component
→ Action
→ Effect
→ API
→ Reducer
→ Store
→ Selector
→ Component

### Vue + Pinia

- Lightweight
- Easy to learn
- Less boilerplate
- Excellent Composition API support
- storeToRefs() keeps reactivity

---

## Conclusion

Pinia provides the simplest and cleanest state management among the three frameworks while maintaining excellent performance.