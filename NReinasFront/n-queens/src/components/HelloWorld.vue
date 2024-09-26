<template>
  <div>
    <input v-model="n" type="number" min="4" />
    <button @click="fetchSolutions">Solve</button>
    <div v-if="solutions.length">
      <div v-for="(solution, index) in solutions" :key="index">
        <div v-for="row in solution" :key="row">
          <span v-for="cell in row" :key="cell">{{ cell }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      n: 8,
      solutions: [],
    };
  },
  methods: {
    async fetchSolutions() {
      fetch("http://127.0.0.1:8000/resolver", {
        method: "POST",
        body: JSON.stringify({ n: this.n }),
        headers: { "Content-type": "application/json" },
      })
      .then(response => response.json())
      .then(json => this.solutions=json.solutions)
      .catch(err => console.log(err));
    },
  },
};
</script>
