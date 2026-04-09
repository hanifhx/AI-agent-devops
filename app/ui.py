import streamlit as st
import requests

st.title("🤖 DevOps AI Agent")

app_type = st.text_input("Enter App Type")

ci_output = ""
k8s_output = ""

# 🔥 CI/CD
if st.button("Generate CI/CD"):
    if app_type:
        with st.spinner("Generating CI/CD..."):
            res = requests.post(
                "http://127.0.0.1:8000/generate-ci",
                json={"app_type": app_type}
            )

            if res.status_code == 200:
                ci_output = res.json().get("ci", "")
                st.subheader("📦 CI/CD Pipeline")
                st.code(ci_output, language="yaml")

                # 🔥 Download button
                st.download_button(
                    label="Download CI.yml",
                    data=ci_output,
                    file_name="ci.yml",
                    mime="text/yaml"
                )
            else:
                st.error("Error generating CI")

# 🔥 Kubernetes
if st.button("Generate K8s"):
    if app_type:
        with st.spinner("Generating K8s..."):
            res = requests.post(
                "http://127.0.0.1:8000/generate-k8s",
                json={"app_type": app_type}
            )

            if res.status_code == 200:
                k8s_output = res.json().get("k8s", "")
                st.subheader("☸️ Kubernetes YAML")
                st.code(k8s_output, language="yaml")

                # 🔥 Download button
                st.download_button(
                    label="Download k8s.yaml",
                    data=k8s_output,
                    file_name="k8s.yaml",
                    mime="text/yaml"
                )
            else:
                st.error("Error generating K8s")