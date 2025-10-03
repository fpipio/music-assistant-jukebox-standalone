# Music Assistant Jukebox - Standalone Web Interface

Interfaccia web standalone per Music Assistant, utilizzabile fuori da Home Assistant.

## Caratteristiche

- 🎵 **Ricerca brani** con filtri per provider (Spotify, Tidal, Qobuz, etc.)
- 📚 **Libreria musicale** con visualizzazione per Playlist, Artisti, Album, Brani
- 🎮 **Player completo** con:
  - Play/Pause/Stop
  - Previous/Next track
  - Seek bar interattiva
  - Controllo volume
  - Progress bar fluida
- 📋 **Gestione coda** con visualizzazione brano corrente e successivo
- 🔍 **Filtri multi-selezione** per provider musicali
- 🎨 **Rilevamento automatico provider** dalle immagini

## Requisiti

- Home Assistant con Music Assistant installato
- Python 3.x (per il server locale)
- Token di accesso a lungo termine di Home Assistant

## Configurazione

1. Apri `jukebox-standalone.html` e modifica la sezione di configurazione:

```javascript
const CONFIG = {
    HA_URL: "http://192.168.77.12:8123",  // URL Home Assistant
    API_TOKEN: "eyJhbGci...",              // Token di accesso
    MEDIA_PLAYER: "media_player.xxx",      // ID del media player
    MUSIC_ASSISTANT_CONFIG_ID: "xxx",      // ID config Music Assistant
    DEFAULT_PLAYLIST: "Party Mix"          // Playlist di default (opzionale)
};
```

2. Configura CORS in Home Assistant (`configuration.yaml`):

```yaml
http:
  cors_allowed_origins:
    - http://localhost:8000
    - http://127.0.0.1:8000
```

## Utilizzo

### Avvio del server

```bash
python server.py
```

Il server sarà disponibile su `http://localhost:8000/jukebox-standalone.html`

## File del progetto

- `jukebox-standalone.html` - Interfaccia web principale
- `server.py` - Server HTTP con supporto CORS
- `MASS_services.yaml` - Documentazione servizi Music Assistant
- `HAMusicAssistantJukebox/` - Integrazione originale per Home Assistant

## Sviluppo

L'interfaccia è completamente standalone e non richiede build o dipendenze Node.js.

## Crediti

- Basato sul progetto [HAMusicAssistantJukebox](https://github.com/DJS91/HAMusicAssistantJukebox)
- Sviluppato con l'assistenza di Claude Code
