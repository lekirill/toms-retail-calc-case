<template>
  <div class="calc">
    <h2>Input data</h2>
    <form @submit.prevent="onSubmit">
      <h4>QTY</h4>
      <input type="number" v-model="qtyLocal" min="0" name="name"/>
      <h4>Unit Price</h4>
      <input type="number" v-model="unit_priceLocal" step="0.0001" min="0" name="name"/>
      <h4>State Code</h4>
      <select v-model="state_codeLocal">
        <option value="UT">UT</option>
        <option value="NV">NV</option>
        <option value="TX">TX</option>
        <option value="AL">AL</option>
        <option value="CA">CA</option>
      </select>
      <p id="notion">all fields are necessary to fill</p>
      <div class="btn-block">
        <button>Calculate</button>
      </div>
    </form>
    <hr>
    <h2>Results</h2>
    <div class="results">
      <h4>Total Price</h4>
      <span class="result">{{ this.total_price }}</span>
      <h4>Discount</h4>
      <span class="result">{{ this.discount }}</span>
      <h4>Discounted Price</h4>
      <span class="result">{{ this.discounted_price }}</span>
      <h4>Final price (+ taxes)</h4>
      <span class="result">{{ this.final_price }}</span>
    </div>
  </div>
</template>

<script>

import axios from "axios"

export default {
  name: "Calc",
  data() {
    return {
      qtyLocal: 0,
      unit_priceLocal: 0,
      state_codeLocal: null,
      result: {},
      total_price: 0,
      discount: 0,
      discounted_price: 0,
      final_price: 0,
    }
  },
  methods: {
    onSubmit() {
      axios
          .post(process.env.VUE_APP_BACKEND_CALCULATE_URL,
              {
                "qty": parseInt(this.qtyLocal),
                "unit_price": parseFloat(this.unit_priceLocal),
                "state_code": this.state_codeLocal
              }
          )
          .then((response) => {
                this.result = response.data.result
                this.total_price = this.result.total_price.toFixed(2);
                this.discount = (this.result.discount_rate * 100).toFixed(2).toString().concat(' %');
                this.discounted_price = this.result.discounted_price.toFixed(2);
                this.final_price = this.result.final_price.toFixed(2);
              },
          )

    }
  }
}
</script>


<style scoped>
div, form, input, select {
  margin: 0 auto;
  outline: none;
  font-family: Roboto, Arial, sans-serif;
  font-size: 14px;
  color: #666;
}

h4 {
  margin: 20px 0 4px;
  font-weight: 400;
}

form {
  width: 30%;
  padding: 20px;
}

input {
  width: calc(40%);
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

select {
  width: calc(40%);
  padding: 7px 0;
  border-radius: 3px;
  border: 1px solid #ccc;
}

.btn-block {
  margin-top: 20px;
  text-align: center;
}

button {
  width: 150px;
  padding: 10px;
  border: none;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
  background-color: #095484;
  font-size: 16px;
  color: #fff;
  cursor: pointer;
}

#notion {
  color: red;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.result {
  font-size: 18px;
}
</style>
