<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>UrlDepot</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.url-modal>Add Url</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Url</th>
              <th scope="col">Category</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(url, index) in urls" :key="index">
              <td>{{ url.url }}</td>
              <td>{{ url.category }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.url-update-modal
                          @click="editUrl(url)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteUrl(url)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addUrlModal"
            id="url-modal"
            url="Add a new url"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-url-group"
                    label="Url:"
                    label-for="form-url-input">
          <b-form-input id="form-url-input"
                        type="text"
                        v-model="addUrlForm.url"
                        required
                        placeholder="Enter url">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-category-group"
                      label="Category:"
                      label-for="form-category-input">
            <b-form-input id="form-category-input"
                          type="text"
                          v-model="addUrlForm.category"
                          required
                          placeholder="Enter category">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editUrlModal"
            id="url-update-modal"
            url="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-url-edit-group"
                    label="Url:"
                    label-for="form-url-edit-input">
          <b-form-input id="form-url-edit-input"
                        type="text"
                        v-model="editForm.url"
                        required
                        placeholder="Enter url">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-category-edit-group"
                      label="Category:"
                      label-for="form-category-edit-input">
            <b-form-input id="form-category-edit-input"
                          type="text"
                          v-model="editForm.category"
                          required
                          placeholder="Enter category">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      urls: [],
      addUrlForm: {
        url: '',
        category: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        url: '',
        category: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getUrls() {
      const path = 'http://localhost:5000/urls';
      axios.get(path)
        .then((res) => {
          this.urls = res.data.urls;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addUrl(payload) {
      const path = 'http://localhost:5000/urls';
      axios.post(path, payload)
        .then(() => {
          this.getUrls();
          this.message = 'Url added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getUrls();
        });
    },
    initForm() {
      this.addUrlForm.url = '';
      this.addUrlForm.category = '';
      this.editForm.id = '';
      this.editForm.url = '';
      this.editForm.category = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addUrlModal.hide();
      const payload = {
        url: this.addUrlForm.url,
        category: this.addUrlForm.category,
      };
      this.addUrl(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addUrlModal.hide();
      this.initForm();
    },
    editUrl(url) {
      this.editForm = url;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUrlModal.hide();
      const payload = {
        url: this.editForm.url,
        category: this.editForm.category,
      };
      this.updateUrl(payload, this.editForm.id);
    },
    updateUrl(payload, urlID) {
      const path = `http://localhost:5000/urls/${urlID}`;
      axios.put(path, payload)
        .then(() => {
          this.getUrls();
          this.message = 'Url updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUrls();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUrlModal.hide();
      this.initForm();
      this.getUrls(); // why?
    },
    removeUrl(urlID) {
      const path = `http://localhost:5000/urls/${urlID}`;
      axios.delete(path)
        .then(() => {
          this.getUrls();
          this.message = 'Url removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUrls();
        });
    },
    onDeleteUrl(url) {
      this.removeUrl(url.id);
    },
  },
  created() {
    this.getUrls();
  },
};
</script>
