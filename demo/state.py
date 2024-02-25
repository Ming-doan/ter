from terapp import State

store = State(init_state=0)

store.reducers(reducer="increase_by_amount",
               action=lambda state, payload: state + payload)
