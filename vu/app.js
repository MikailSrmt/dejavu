new Vue({
  el: "#vue-app",
  data: {
    name: "Mikail",
    job: "Software Engineer",
    website: "https://www.github.com/",
    websiteTag: '<a href="https://www.github.com/mikailseremet/"> My GitHub</a>'
  },
  methods: {
    greet: function(time) {
      return "Good " + time + " " + this.name;
    }
  }
});
