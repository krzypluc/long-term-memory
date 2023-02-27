<script lang="ts">
    import type { Person } from "../types/searchResponseData";
    export let row: Person;
</script>

<div class="box">
    <article class="media">
        <div class="media-left">
          <figure class="image is-64x64">
            <img src="https://bulma.io/images/placeholders/128x128.png">
          </figure>
        </div>
        <div class="media-content">
          <div class="content">
            <p>
              <strong>{row.firstname} {row.surname}</strong> <small>@johnsmith</small> <small>31m</small>
              <br>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean efficitur sit amet massa fringilla egestas. Nullam condimentum luctus turpis.
            </p>
          </div>
        </div>
      </article>
</div>