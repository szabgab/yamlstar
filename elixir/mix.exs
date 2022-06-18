defmodule YAMLStar.MixProject do
  use Mix.Project

  def project do
    [
      app: :yamlstar,
      version: "0.0.1",
      description: "A cross-language, common API YAML reference framework",
      elixir: "~> 1.12",
      package: package(),
      deps: deps()
    ]
  end

  def package do
    [
      licenses: ["MIT"],
      files: ~w(lib test mix.exs README*),
      maintainers: ["Ingy döt Net <ingy@ingy.net>"],
      links: %{"GitHub" => "https://github.com/yaml/yamlstar"}
    ]
  end

  defp deps do
    [
      {:ex_doc, ">= 0.0.0", only: :dev, runtime: false}
    ]
  end

end
